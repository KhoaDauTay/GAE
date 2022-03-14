import {AfterViewInit, Component, ElementRef, Input, ViewChild} from "@angular/core";
import {createPopper} from "@popperjs/core";
import { Router} from "@angular/router";
@Component({
  selector: "app-application-dropdown",
  templateUrl: "./application-dropdown.component.html",
})
export class ApplicationDropdownComponent implements AfterViewInit {
  constructor(private router: Router,) {
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
}
