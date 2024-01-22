import { Injectable } from "@angular/core";
import { Store, StoreConfig } from "@datorama/akita";
import { TokenService} from "../services";
import {UsersService} from "./users/users.service";
import {User} from "./users/user.model";
import {environment} from "../../../environments/environment";

export interface AuthenticationState {
  isLoggedIn: boolean;
  userId?: number;
}

export function createInitialState(): AuthenticationState {
  return {
    isLoggedIn: false,
    userId: null
  };
}

@Injectable({ providedIn: "root" })
@StoreConfig({ name: "authentication" })
export class AuthenticationStore extends Store<AuthenticationState> {
  constructor(
    private readonly tokenService: TokenService,
    private readonly userService: UsersService
  ) {
    super(createInitialState());
  }
  async setIsLoggedIn(value: boolean): Promise<void> {
    const prevValue = this.getIsLoggedIn();
    if (value === prevValue) {
      return;
    }

    const userId = value ? await this.tokenService.getUserId() : null;

    this.update({
      isLoggedIn: value,
      userId
    });
    if (value) {
      this.userService.get(userId).subscribe(
        (user: User) => localStorage.setItem(environment.USER_STORAGE_KEY, JSON.stringify(user))
      );
    }
  }

  getIsLoggedIn(): boolean {
    return this.getValue().isLoggedIn;
  }
  getUserId() {
    return !!this.getValue().userId;
  }
}
