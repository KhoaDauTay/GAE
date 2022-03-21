import {Component, Input, OnInit} from "@angular/core";
import {User} from "../state/users/user.model";
import {ActivatedRoute} from "@angular/router";
import {FormBuilder, Validators} from "@angular/forms";
import {AlertService} from "../../alert";
import {UsersService} from "../state/users/users.service";

@Component({
  selector: "app-card-settings",
  templateUrl: "./card-settings.component.html",
})
export class CardSettingsComponent implements OnInit {
  @Input() user: User;
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  constructor(
    private route: ActivatedRoute,
    private readonly formBuilder: FormBuilder,
    public alertService: AlertService,
    private userService: UsersService,
  ) {}
  userForm = this.formBuilder.group({
    name: ["", Validators.required],
    first_name: [""],
    last_name: [""],
    role: [""],
    client: this.formBuilder.group({
      address: [""],
      city: [""],
      country: [""],
      postal_code: [""],
      about_me: [""],
    })
  });
  Roles: Array<string> = ["ADMIN", "STAFF", "STUDENT", "MANAGER", "SECURITY" ];
  defaultRole: string;
  ngOnInit(): void {
    this.defaultRole = this.user.role;
    this.Roles.forEach((role,index)=>{
      if(role === this.defaultRole){
        this.Roles.splice(index,1);
      }
    });
    this.loadFormGroup();
  }

  private loadFormGroup() {
    this.userForm.patchValue(
      {
        name: this.user.name,
        first_name: this.user.first_name,
        last_name: this.user.last_name,
        role: this.defaultRole,
      }
    );
    this.userForm.get("client").patchValue({
      address: this.user.client.address,
      city: this.user.client.city,
      country: this.user.client.country,
      postal_code: this.user.client.postal_code,
      about_me: this.user.client.about_me,
    });

  }
  get roleValue() {
    return this.userForm.get("role");
  }
  changeRole($event: any) {
    this.roleValue?.setValue($event.target.value, {
      onlySelf: true,
    });
  }
  onSubmit() {
    if (this.userForm.invalid) {
      this.alertService.error(`Please check your input`, this.options);
      return;
    }
    const userUpdate = this.userForm.value;
    console.log(userUpdate);
  }
}
