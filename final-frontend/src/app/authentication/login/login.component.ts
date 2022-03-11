import { Component, OnInit } from "@angular/core";
import {AuthenticationService} from "../services";
import {AuthenticationQuery} from "../state/authentication.query";
import {Router} from "@angular/router";
import {FormBuilder, Validators} from "@angular/forms";
import {Credentials} from "../state/authentication.modell";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
})
export class LoginComponent implements OnInit {
  loginForm = this.formBuilder.group({
    username: ["", Validators.required],
    password: ["", Validators.required]
  });
  constructor(
    private readonly authService: AuthenticationService,
    private readonly authQuery: AuthenticationQuery,
    private readonly router: Router,
    private readonly formBuilder: FormBuilder
  ) {}

  login() {
    if (!this.loginForm.valid) {
      alert("Please enter required login data Invalid Input");
      return;
    }
    const credentials: Credentials = this.loginForm.value;

    this.authService.login(credentials).subscribe(
      () => this.router.navigateByUrl("/admin"),
    );
  }
  ngOnInit(): void {}
}
