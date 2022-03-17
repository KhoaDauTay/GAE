import {Component, Input, OnInit} from "@angular/core";
import {User} from "../state/users/user.model";

@Component({
  selector: "app-card-settings",
  templateUrl: "./card-settings.component.html",
})
export class CardSettingsComponent implements OnInit {
  @Input() user: User;
  constructor() {}

  ngOnInit(): void {}
}
