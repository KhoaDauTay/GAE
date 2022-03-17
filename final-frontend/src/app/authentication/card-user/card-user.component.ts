import { Component, OnInit, Input } from "@angular/core";
import {UsersService} from "../state/users/users.service";
import {UsersQuery} from "../state/users/users.query";
import {User} from "../state/users/user.model";
import {Observable} from "rxjs";

@Component({
  selector: "app-card-user",
  templateUrl: "./card-user.component.html",
})
export class CardUserComponent implements OnInit {
  @Input()
  get color(): string {
    return this._color;
  }
  set color(color: string) {
    this._color = color !== "light" && color !== "dark" ? "light" : color;
  }
  private _color = "light";
  users$: Observable<User[]>;
  constructor(
    private userService: UsersService,
    private userQuery: UsersQuery,
  ) {}

  ngOnInit(): void {
    this.userService.get().subscribe();
    this.users$ = this.userQuery.selectAll();
  }
}
