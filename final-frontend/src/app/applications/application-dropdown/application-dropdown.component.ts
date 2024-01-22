import {AfterViewInit, Component, ElementRef, Input, ViewChild} from "@angular/core";
import {createPopper} from "@popperjs/core";
import { Router} from "@angular/router";
import {ApplicationsService} from "../state/applications.service";
import {AlertService} from "../../alert";
@Component({
  selector: "app-application-dropdown",
  templateUrl: "./application-dropdown.component.html",
})
export class ApplicationDropdownComponent implements AfterViewInit {
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  showModal = false;
  constructor(
    private router: Router,
    private applicationService: ApplicationsService,
    public alertService: AlertService) {
  }
  @Input() applicationId: number;
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

  navigateSettings() {
    this.router.navigate(["/admin/applications", this.applicationId])
  }
  toggleModal(){
    this.showModal = !this.showModal;
  }

  deleteApplication() {
    this.applicationService.delete(this.applicationId).subscribe(
      (() => {
        this.alertService.success(`Delete a row successfully!!!`, this.options);
        this.toggleModal();
      })
    )
  }
}
