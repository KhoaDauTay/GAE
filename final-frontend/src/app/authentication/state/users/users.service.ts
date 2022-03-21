import {Injectable} from "@angular/core";
import {NgEntityService} from "@datorama/akita-ng-entity-service";
import {UsersState, UsersStore} from "./users.store";
import {User} from "./user.model";
import {HttpClient} from "@angular/common/http";
import {tap} from "rxjs/operators";
import {catchError, throwError} from "rxjs";

@Injectable({ providedIn: "root" })
export class UsersService extends NgEntityService<UsersState> {

  constructor(protected store: UsersStore) {
    super(store);
  }
  inviteUser(user){
    const http: HttpClient = this.getHttp();
    return http.post<User | null>( `${this.baseUrl}/users/invite`, user)
      .pipe(
        catchError((err) => {
          return throwError(err.error);
        }),
        tap(
          users => this.store.add(users)
        )
      );
  }
}
