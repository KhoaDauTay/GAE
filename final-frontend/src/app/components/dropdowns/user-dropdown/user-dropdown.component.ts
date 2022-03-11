import {Component, AfterViewInit, ViewChild, ElementRef, OnInit} from "@angular/core";
import { createPopper } from "@popperjs/core";
import {AuthenticationService} from "../../../authentication/services";
import {AuthenticationQuery} from "../../../authentication/state/authentication.query";
import {Router} from "@angular/router";
import {UsersQuery} from "../../../authentication/state/users/users.query";
import {User} from "../../../authentication/state/users/user.model";

@Component({
  selector: "app-user-dropdown",
  templateUrl: "./user-dropdown.component.html",
})
export class UserDropdownComponent implements OnInit,AfterViewInit {
  constructor(
    private readonly authService: AuthenticationService,
    private readonly authQuery: AuthenticationQuery,
    private readonly router: Router,
  ) {
  }
  avatar: string;
  dropdownPopoverShow = false;
  @ViewChild("btnDropdownRef", { static: false }) btnDropdownRef: ElementRef;
  @ViewChild("popoverDropdownRef", { static: false })
  popoverDropdownRef: ElementRef;
  ngOnInit(): void {
    this.authQuery.user$.subscribe(
      (user) => this.avatar = user.avatar
    );
  }
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
    if (this.dropdownPopoverShow) {
      this.dropdownPopoverShow = false;
    } else {
      this.dropdownPopoverShow = true;
    }
  }

  logout() {
    this.authService.logout();
    if(!this.authQuery.isLoggedIn()){
      this.router.navigate(["/login"])
    }
  }

}
