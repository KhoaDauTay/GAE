import { Component, OnInit } from "@angular/core";
import {RequestsService} from "../../../monitor/state/requests.service";
import {RequestsQuery} from "../../../monitor/state/requests.query";
import {Observable} from "rxjs";
import {Request} from "../../../monitor/state/request.model";
@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
})
export class DashboardComponent implements OnInit {
  constructor(
    private requestService: RequestsService,
    private requestQuery: RequestsQuery
  ) {}
  data$:  Observable<Request[]>
  ngOnInit() {
    this.requestService.get().subscribe(
      () => {
          this.data$ = this.requestQuery.selectAll()
        }
    )
  }
}
