import {AfterViewInit, Component, ElementRef, Input, ViewChild} from "@angular/core";
import {createPopper} from "@popperjs/core";
import {AlertService} from "../../alert";
import {Router} from "@angular/router";
import {RolesService} from "../state/roles.service";

@Component({
  selector: "app-role-dropdown",
  templateUrl: "./role-dropdown.component.html",
})
export class RoleDropdownComponent implements AfterViewInit {
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  @Input() roleId: number | string;
  showModal = false;
  constructor(
    public alertService: AlertService,
    private roleService: RolesService,
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

  deleteRole(event) {
    this.roleService.delete(this.roleId).subscribe(
      (() => {
        this.alertService.info(`Delete a row successfully!!!`, this.options);
        this.toggleModal(event);
      })
    )
  }
  navigateRole() {
    this.router.navigate(["/admin/roles", this.roleId]);
  }
}
