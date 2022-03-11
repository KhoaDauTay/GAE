import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import {HTTP_INTERCEPTORS} from "@angular/common/http";
import {AuthenticationInterceptor} from "./services";
import {ReactiveFormsModule} from "@angular/forms";
import {LoginComponent} from "./login/login.component";
import {AuthNavbarComponent} from "../components/navbars/auth-navbar/auth-navbar.component";
import {FooterSmallComponent} from "../components/footers/footer-small/footer-small.component";
import {RouterModule} from "@angular/router";



@NgModule({
  declarations: [
    LoginComponent,
    AuthNavbarComponent,
    FooterSmallComponent
  ],
  exports: [
    LoginComponent
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
