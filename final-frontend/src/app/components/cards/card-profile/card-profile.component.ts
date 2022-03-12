import {Component, Input, OnInit} from "@angular/core";
import {User} from "../../../authentication/state/users/user.model";

@Component({
  selector: "app-card-profile",
  templateUrl: "./card-profile.component.html",
})
export class CardProfileComponent implements OnInit {
  @Input() user: User;
  constructor(

  ) {}

  ngOnInit(): void {
  }
}
