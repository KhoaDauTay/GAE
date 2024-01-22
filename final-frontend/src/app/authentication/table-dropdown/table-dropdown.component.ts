import {Component, AfterViewInit, ViewChild, ElementRef, Input} from "@angular/core";
import { createPopper } from "@popperjs/core";
import {AlertService} from "../../alert";
import {UsersService} from "../state/users/users.service";

@Component({
  selector: "app-table-dropdown",
  templateUrl: "./table-dropdown.component.html",
})
export class TableDropdownComponent implements AfterViewInit {
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  constructor(
    public alertService: AlertService,
    private userService: UsersService
  ) {}
  @Input() userId;
  showModal = false;
  dropdownPopoverShow = false;
  @ViewChild("btnDropdownRef", { static: false }) btnDropdownRef: ElementRef;
  @ViewChild("popoverDropdownRef", { static: false })
  popoverDropdownRef: ElementRef;
  ngAfterViewInit() {
    createPopper(
      this.btnDropdownRef.nativeElement,
      this.popoverDropdownRef.nativeElement,
      {
        placement: "bottom-start",
      }
    );
  }

  toggleDropdown(event) {
    event.preventDefault();
    this.dropdownPopoverShow = !this.dropdownPopoverShow;
  }
  toggleModal(){
    this.showModal = !this.showModal;
    this.dropdownPopoverShow = !this.dropdownPopoverShow;
  }
  deleteUser() {
    this.userService.delete(this.userId).subscribe(
      (() => {
        this.alertService.success(`Delete a user successfully!!!`, this.options);
        this.toggleModal();
      })
    )
  }
}
