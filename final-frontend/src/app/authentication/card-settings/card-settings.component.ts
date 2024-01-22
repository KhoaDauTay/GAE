import {Component, EventEmitter, Input, OnInit, Output} from "@angular/core";
import {User} from "../state/users/user.model";
import {ActivatedRoute} from "@angular/router";
import {FormBuilder, Validators} from "@angular/forms";
import {AlertService} from "../../alert";
import {UsersService} from "../state/users/users.service";
import {UsersQuery} from "../state/users/users.query";

@Component({
  selector: "app-card-settings",
  templateUrl: "./card-settings.component.html",
})
export class CardSettingsComponent implements OnInit {
  @Input() user: User;
  @Output() userChange = new EventEmitter<User>();
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  userId: string;
  constructor(
    private route: ActivatedRoute,
    private readonly formBuilder: FormBuilder,
    public alertService: AlertService,
    private userService: UsersService,
    private userQuery: UsersQuery,
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
    this.userId = this.route.snapshot.paramMap.get("id");
    if(!this.userId){
      this.userId = this.user.id
    }
    this.userService.get(this.userId).subscribe(
      () => {
        this.user = this.userQuery.getEntity(this.userId)
        this.defaultRole = this.user.role;
        this.Roles.forEach((role,index)=>{
          if(role === this.defaultRole){
            this.Roles.splice(index,1);
          }
        });
        this.loadFormGroup();
      }
    )
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
    this.userService.update(this.user.id, userUpdate).subscribe(
      () => {
        this.alertService.success(`${this.userForm.get("name").value.toString()} update successfully!!!`, this.options);
        this.user = this.userQuery.getEntity(this.userId);
        this.userChange.emit(this.user);
      },
      error => {
        this.alertService.error(`Field: ${error?.email[0]}`, this.options);
      }
    )
  }
}
