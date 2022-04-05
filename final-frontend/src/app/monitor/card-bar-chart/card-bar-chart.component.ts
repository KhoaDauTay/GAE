import {Component, OnInit, AfterViewInit, Input} from "@angular/core";
import Chart from "chart.js";
import {Request} from "../state/request.model";
import {Uris} from "../state/uris.model";

@Component({
  selector: "app-card-bar-chart",
  templateUrl: "./card-bar-chart.component.html",
})
export class CardBarChartComponent implements OnInit, AfterViewInit {
  constructor(
  ) {}
  @Input() data: Request[];
  ngOnInit() {
  }
  ngAfterViewInit() {
    const config = {
      type: "bar",
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: this.data[0].year,
            backgroundColor: "#ed64a6",
            borderColor: "#ed64a6",
            data: [
              this.data[0].january,
              this.data[0].february,
              this.data[0].march,
              this.data[0].april,
              this.data[0].may,
              this.data[0].june,
              this.data[0].july,
            ],
            fill: false,
            barThickness: 8,
          },
          {
            label: this.data[1].year,
            fill: false,
            backgroundColor: "#4c51bf",
            borderColor: "#4c51bf",
            data: [
              this.data[1].january,
              this.data[1].february,
              this.data[1].march,
              this.data[1].april,
              this.data[1].may,
              this.data[1].june,
              this.data[1].july,
            ],
            barThickness: 8,
          },
        ],
      },
      options: {
        maintainAspectRatio: false,
        responsive: true,
        title: {
          display: false,
          text: "Orders Chart",
        },
        tooltips: {
          mode: "index",
          intersect: false,
        },
        hover: {
          mode: "nearest",
          intersect: true,
        },
        legend: {
          labels: {
            fontColor: "rgba(0,0,0,.4)",
          },
          align: "end",
          position: "bottom",
        },
        scales: {
          xAxes: [
            {
              display: false,
              scaleLabel: {
                display: true,
                labelString: "Month",
              },
              gridLines: {
                borderDash: [2],
                borderDashOffset: [2],
                color: "rgba(33, 37, 41, 0.3)",
                zeroLineColor: "rgba(33, 37, 41, 0.3)",
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2],
              },
            },
          ],
          yAxes: [
            {
              display: true,
              scaleLabel: {
                display: false,
                labelString: "Value",
              },
              gridLines: {
                borderDash: [2],
                drawBorder: false,
                borderDashOffset: [2],
                color: "rgba(33, 37, 41, 0.2)",
                zeroLineColor: "rgba(33, 37, 41, 0.15)",
                zeroLineBorderDash: [2],
                zeroLineBorderDashOffset: [2],
              },
            },
          ],
        },
      },
    };
    let ctx: any = document.getElementById("bar-chart");
    ctx = ctx.getContext("2d");
    new Chart(ctx, config);
  }
}
