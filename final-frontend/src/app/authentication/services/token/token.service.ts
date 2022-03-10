import {Injectable} from "@angular/core";
import {JwtHelperService} from "@auth0/angular-jwt";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {JwtPayload, Tokens} from "./token.model";
import {environment} from "../../../../environments/environment";
import {catchError, Observable, of} from "rxjs";
import {tap} from "rxjs/operators";
@Injectable({
  providedIn: "root"
})
export class TokenService {

  private readonly TOKEN_STORAGE_KEY = "auth_tokens";
  private readonly REFRESH_WINDOW_SECONDS = 600;

  private jwtHelper = new JwtHelperService();

  constructor(
    private http: HttpClient
  ) {}

  setTokens(tokens: Tokens) {
    localStorage.setItem(this.TOKEN_STORAGE_KEY, JSON.stringify(tokens));
  }

  private getTokens(): Tokens | null {
    const tokenJSON = localStorage.getItem(this.TOKEN_STORAGE_KEY);
    console.log(tokenJSON);
    return tokenJSON ? JSON.parse(tokenJSON) as Tokens : null;
  }

  getRefreshToken(): string {
    const tokens = this.getTokens();
    return tokens.refresh;
  }

  async getAccessToken(): Promise<string | null> {
    let tokens = this.getTokens();

    if (!tokens) {
      return null;
    }

    const accessToken = tokens.access;

    if (!this.isTokenAboutToExpire(accessToken)) {
      return accessToken;
    }

    tokens = await this.refreshTokens(accessToken, tokens.refresh).toPromise();

    return tokens && tokens.access;
  }

  async getUserId(): Promise<number | null> {
    const accessToken = await this.getAccessToken();

    if (!accessToken) {
      return null;
    }

    const jwtPayload: JwtPayload = this.jwtHelper.decodeToken(accessToken);

    return +jwtPayload.user_id;
  }

  removeTokens() {
    localStorage.removeItem(this.TOKEN_STORAGE_KEY);
  }

  private refreshTokens(accessToken: string, refreshToken: string): Observable<Tokens | null> {
    const httpOptions = {
      headers: new HttpHeaders({
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`
      })
    }
    const body = {
      refresh: `${refreshToken}`
    }
    return this.http.post<Tokens | null>( environment.apiUrl + "token/refresh/", body, httpOptions)
      .pipe(
        catchError(
          () => of(null)
        ),
        tap(
          tokens => this.setTokens(tokens)
        )
      );
  }

  private isTokenAboutToExpire(accessToken: string): boolean {
    return this.jwtHelper.isTokenExpired(accessToken, this.REFRESH_WINDOW_SECONDS);
  }

}
