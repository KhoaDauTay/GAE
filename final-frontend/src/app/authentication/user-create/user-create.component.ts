import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-user-create",
  templateUrl: "./user-create.component.html",
})
export class UserCreateComponent implements OnInit {
  showModal = false;
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  constructor() { }

  ngOnInit(): void {
  }
  toggleModal(){
    this.showModal = !this.showModal;
  }
}
