import {Component, AfterViewInit, ViewChild, ElementRef, OnInit} from "@angular/core";
import { createPopper } from "@popperjs/core";
import {AuthenticationService} from "../../../authentication/services";
import {AuthenticationQuery} from "../../../authentication/state/authentication.query";
import {Router} from "@angular/router";
import {UsersQuery} from "../../../authentication/state/users/users.query";
import {User} from "../../../authentication/state/users/user.model";
import {environment} from "../../../../environments/environment";

@Component({
  selector: "app-user-dropdown",
  templateUrl: "./user-dropdown.component.html",
})
export class UserDropdownComponent implements OnInit,AfterViewInit {
  constructor(
    private readonly authService: AuthenticationService,
    private readonly userQuery: UsersQuery,
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
    const userJson: string = localStorage.getItem(environment.USER_STORAGE_KEY)
    if (userJson) {
      const user: User = JSON.parse(userJson);
      this.avatar = user.avatar;
    } else {
      this.avatar = this.userQuery.getAvatar(this.authQuery.userId());
    }
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
    this.dropdownPopoverShow = !this.dropdownPopoverShow;
  }

  logout() {
    this.authService.logout();
    if(!this.authQuery.isLoggedIn()){
      this.router.navigate(["/login"])
    }
  }

}
