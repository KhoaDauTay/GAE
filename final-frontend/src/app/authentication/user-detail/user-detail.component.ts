import { Component, OnInit } from "@angular/core";
import {User} from "../state/users/user.model";
import {UsersQuery} from "../state/users/users.query";
import {ActivatedRoute} from "@angular/router";
import {UsersService} from "../state/users/users.service";

@Component({
  selector: "app-user-detail",
  templateUrl: "./user-detail.component.html",
})
export class UserDetailComponent implements OnInit {
  user: User
  userId: string
  constructor(
    private route: ActivatedRoute,
    private userQuery: UsersQuery,
    private userService: UsersService
  ) {}

  ngOnInit(): void {
    this.userId = this.route.snapshot.paramMap.get("id");
    this.userService.get(this.userId).subscribe(
      () => {
        this.user = this.userQuery.getEntity(this.userId);
      }
    )
  }
  changeValue(user: User){
    this.user = user;
  }
}
