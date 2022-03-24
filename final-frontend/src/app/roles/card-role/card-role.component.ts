import {Component, Input, OnInit} from "@angular/core";
import {Observable} from "rxjs";
import {Role} from "../state/role.model";
import {RolesService} from "../state/roles.service";
import {RolesQuery} from "../state/roles.query";

@Component({
  selector: "app-card-role",
  templateUrl: "./card-role.component.html",
})
export class CardRoleComponent implements OnInit {
  @Input()
  get color(): string {
    return this._color;
  }
  set color(color: string) {
    this._color = color !== "light" && color !== "dark" ? "light" : color;
  }
  private _color = "light";
  constructor(
    private roleService: RolesService,
    private roleQuery: RolesQuery
  ) {
  }
  roles$: Observable<Role[]>;
  ngOnInit(): void {
    this.roleService.get().subscribe();
    this.roles$ = this.roleQuery.selectAll();
  }
}
