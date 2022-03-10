import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import { Injectable } from "@angular/core";
import { tap } from "rxjs/operators";
import { AuthenticationStore } from "../state/authentication.store";
import {TokenService} from "./token";
import {Credentials} from "../state/authentication.modell";
import {catchError, Observable, throwError} from "rxjs";
import {Tokens} from "./token";
import {environment} from "../../../environments/environment";
import {setLoading} from "@datorama/akita";

@Injectable({ providedIn: "root" })
export class AuthenticationService {

  constructor(
    private authenticationStore: AuthenticationStore,
    private http: HttpClient,
    private tokenService: TokenService,
  ) {
  }
  login(credentials: Credentials): Observable<Tokens> {
    this.authenticationStore.setLoading(true);

    return this.http.post<Tokens>(environment.apiUrl + "token/", credentials)
      .pipe(
        setLoading(this.authenticationStore),
        catchError(
          (e: HttpErrorResponse) => throwError(e.error?.message ?? "Server Error")
        ),
        tap(
          tokens => {
            this.tokenService.setTokens(tokens);
            this.authenticationStore.setIsLoggedIn(true);
          }
        )
      );
  }

  logout(): void {
    this.authenticationStore.setIsLoggedIn(false);
    this.tokenService.removeTokens();
  }

  async isLoggedIn(): Promise<boolean> {
    const accessToken = await this.tokenService.getAccessToken();

    return !!accessToken;
  }

}
