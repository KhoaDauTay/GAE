import { Injectable } from "@angular/core";
import { Store, StoreConfig } from "@datorama/akita";
import {TokenService} from "../services";
import {UsersService} from "./users/users.service";

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
      this.userService.get("me").subscribe();
    }
  }

  getIsLoggedIn(): boolean {
    return this.getValue().isLoggedIn;
  }
}
