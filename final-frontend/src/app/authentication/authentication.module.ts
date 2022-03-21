import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import {HTTP_INTERCEPTORS} from "@angular/common/http";
import {AuthenticationInterceptor} from "./services";
import {ReactiveFormsModule} from "@angular/forms";
import {LoginComponent} from "./login/login.component";
import {AuthNavbarComponent} from "../components/navbars/auth-navbar/auth-navbar.component";
import {FooterSmallComponent} from "../components/footers/footer-small/footer-small.component";
import {RouterModule} from "@angular/router";
import { InviteUsersComponent } from "./invite-users/invite-users.component";
import {ProfileComponent} from "./profile/profile.component";
import {CardUserComponent} from "./card-user/card-user.component";
import {CardProfileComponent} from "./card-profile/card-profile.component";
import {UserDropdownComponent} from "./user-dropdown/user-dropdown.component";
import {TableDropdownComponent} from "./table-dropdown/table-dropdown.component";
import {CardSettingsComponent} from "./card-settings/card-settings.component";
import { UserCreateComponent } from "./user-create/user-create.component";
import { UserDetailComponent } from "./user-detail/user-detail.component";



@NgModule({
  declarations: [
    UserDropdownComponent,
    TableDropdownComponent,
    LoginComponent,
    AuthNavbarComponent,
    FooterSmallComponent,
    InviteUsersComponent,
    ProfileComponent,
    CardUserComponent,
    CardProfileComponent,
    CardSettingsComponent,
    UserCreateComponent,
    UserDetailComponent,
  ],
  exports: [
    LoginComponent,
    CardUserComponent,
    UserDropdownComponent,
    CardSettingsComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterModule,
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: AuthenticationInterceptor,
    multi: true
  }]
})
export class AuthenticationModule { }
