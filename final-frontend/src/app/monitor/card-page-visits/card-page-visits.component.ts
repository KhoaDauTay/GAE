import {Component, OnInit} from "@angular/core";
import {UrisService} from "../state/uris.service";
import {Uris} from "../state/uris.model";

@Component({
  selector: "app-card-page-visits",
  templateUrl: "./card-page-visits.component.html",
})
export class CardPageVisitsComponent implements OnInit {
  constructor(
    private uriService: UrisService,
  ) {}
  data$: Uris[]
  ngOnInit(): void {
    this.uriService.get().subscribe(
      (value: Uris[]) => {
        this.data$ = value.map(
          item => ({
            ...item,
            rate: Math.floor(Math.random() * (100 - 1 + 1) + 1),
            unique: Math.floor(Math.random() * (20 - 1 + 1) + 1),
          })
        )
        this.data$ = this.data$.map(
          item => ({
            ...item,
            arrow: item.rate >= 0 && item.rate < 50 ? "down" : "up",
            color: item.rate >= 0 && item.rate < 50 ? "red" : "emerald"
          })
        )
      }
    )
  }
}
