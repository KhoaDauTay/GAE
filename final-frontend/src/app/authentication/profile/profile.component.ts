import { Component, OnInit } from "@angular/core";
import {User} from "../state/users/user.model";
import {AuthenticationQuery} from "../state/authentication.query";
import {UsersQuery} from "../state/users/users.query";
import {environment} from "../../../environments/environment";

@Component({
  selector: "app-profile",
  templateUrl: "./profile.component.html",
})
export class ProfileComponent implements OnInit {
  user: User
  constructor(
    private authQuery: AuthenticationQuery,
    private userQuery: UsersQuery
  ) {}

  ngOnInit(): void {
    const userJson: string = localStorage.getItem(environment.USER_STORAGE_KEY)
    if (userJson) {
      this.user = JSON.parse(userJson);
    } else {
      this.user = this.userQuery.getEntity(this.authQuery.userId());
    }
  }
}
