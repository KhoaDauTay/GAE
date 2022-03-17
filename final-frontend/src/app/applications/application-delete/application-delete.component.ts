import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-application-delete",
  templateUrl: "./application-delete.component.html",
})
export class ApplicationDeleteComponent implements OnInit {
  showModal = false;
  constructor() { }

  ngOnInit(): void {
  }
  toggleModal(){
    this.showModal = !this.showModal;
  }
}
