import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import {CardBarChartComponent} from "./card-bar-chart/card-bar-chart.component";
import {CardLineChartComponent} from "./card-line-chart/card-line-chart.component";
import {CardPageVisitsComponent} from "./card-page-visits/card-page-visits.component";



@NgModule({
  declarations: [
    CardBarChartComponent,
    CardLineChartComponent,
    CardPageVisitsComponent
  ],
  exports: [
    CardBarChartComponent,
    CardLineChartComponent,
    CardPageVisitsComponent
  ],
  imports: [
    CommonModule
  ]
})
export class MonitorModule { }
