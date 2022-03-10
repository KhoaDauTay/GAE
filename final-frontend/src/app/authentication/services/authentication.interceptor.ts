import {Injectable} from "@angular/core";
import {HttpHandler, HttpInterceptor, HttpRequest} from "@angular/common/http";
import {TokenService} from "./token";
import {AuthenticationStore} from "../state/authentication.store";
import {Router} from "@angular/router";
import {mergeMap, throwError, from} from "rxjs";
import {environment} from "../../../environments/environment";

@Injectable()
export class AuthenticationInterceptor implements HttpInterceptor {

  private readonly EXCLUDED_PATHS = ["token/", "token/refresh/"];

  constructor(
    private tokenService: TokenService,
    private authenticationStore: AuthenticationStore,
    private router: Router
  ) {}

  intercept(request: HttpRequest<any>, next: HttpHandler) {
    if (this.isExcludedUrl(request.url)) {
      return next.handle(request);
    }
    // const authToken = this.tokenService.getAccessToken();
    // request = request.clone({
    //   setHeaders: {
    //     Authorization: "Bearer " + authToken
    //   }
    // });
    // return next.handle(request);
    return from(this.tokenService.getAccessToken())
      .pipe(
        mergeMap(token => {
          if (token) {
            // tslint:disable-next-line:one-variable-per-declaration
            const headers = request.headers.set("Authorization", `Bearer ${token}`),
              authorizedRequest = request.clone({
                headers
              });
            return next.handle(authorizedRequest);
          } else {
            this.authenticationStore.setIsLoggedIn(false);
            this.router.navigate(["/"], {
              skipLocationChange: true
            });
            return throwError("Not authorized");
          }
        })
      );
  }

  private isExcludedUrl(url: string) {
    // tslint:disable-next-line:one-variable-per-declaration
    const isApiUrl = url.startsWith(environment.apiUrl),
      isExcludedPath = this.EXCLUDED_PATHS
        .find(path => url.includes(path));

    return !isApiUrl || isExcludedPath;
  }

}
