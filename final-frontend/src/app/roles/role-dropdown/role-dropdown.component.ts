import {AfterViewInit, Component, ElementRef, Input, ViewChild} from "@angular/core";
import {createPopper} from "@popperjs/core";
import {AlertService} from "../../alert";
import {Router} from "@angular/router";

@Component({
  selector: "app-role-dropdown",
  templateUrl: "./role-dropdown.component.html",
})
export class RoleDropdownComponent implements AfterViewInit {
  @Input() roleId: number | string;
  showModal = false;
  constructor(
    public alertService: AlertService,
    private router: Router,
  ) { }
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
  toggleModal(event){
    this.showModal = !this.showModal;
    this.toggleDropdown(event);
  }

  deleteRole() {

  }

  navigateRole() {
    this.router.navigate(["/admin/roles", this.roleId]);
  }
}
