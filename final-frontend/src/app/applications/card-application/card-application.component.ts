import {Component, Input, OnInit} from "@angular/core";
import {Observable} from "rxjs";
import {Application} from "../state/application.model";
import {ApplicationsService} from "../state/applications.service";
import {ApplicationsQuery} from "../state/applications.query";
import {ApplicationsStore} from "../state/applications.store";

@Component({
  selector: "app-card-application",
  templateUrl: "./card-application.component.html",
})
export class CardApplicationComponent implements OnInit {
  @Input()
  get color(): string {
    return this._color;
  }
  set color(color: string) {
    this._color = color !== "light" && color !== "dark" ? "light" : color;
  }
  private _color = "light";
  applications$: Observable<Application[]>;
  constructor(
    private applicationService: ApplicationsService,
    private applicationQuery: ApplicationsQuery,
    private applicationStore: ApplicationsStore,
  ) {}

  ngOnInit(): void {
    this.applicationService.get().subscribe();
    this.applications$ = this.applicationQuery.selectAll();
    console.log(this.applicationStore.getValue());
  }

}
