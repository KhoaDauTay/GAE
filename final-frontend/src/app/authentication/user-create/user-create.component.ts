import { Component, OnInit } from "@angular/core";
import {FormBuilder, Validators} from "@angular/forms";
import {AlertService} from "../../alert";
import {UsersService} from "../state/users/users.service";

@Component({
  selector: "app-user-create",
  templateUrl: "./user-create.component.html",
})
export class UserCreateComponent implements OnInit {
  showModal = false;
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  inviteForm = this.formBuilder.group({
    name: ["", Validators.required],
    email: ["", [Validators.required, Validators.email]],
    role: [""],
  });
  Roles: Array<string> = ["ADMIN", "STAFF", "STUDENT", "MANAGER", "SECURITY" ];
  defaultRole: string;
  constructor(
    private formBuilder: FormBuilder,
    public alertService: AlertService,
    private userService: UsersService,
    ) {}

  ngOnInit(): void {
    this.defaultRole = "STAFF";
    this.Roles.forEach((role,index)=>{
      if(role === this.defaultRole){
        this.Roles.splice(index,1);
      }
    });
    this.loadFormGroup();
  }
  toggleModal(){
    this.showModal = !this.showModal;
  }

  loadFormGroup() {
    this.inviteForm.setValue(
      {
        name: "Example name",
        email: "example@gmail.com",
        role: this.defaultRole,
      }
    );
  }
  get roleValue() {
    return this.inviteForm.get("role");
  }
  changeRole($event: any) {
    this.roleValue?.setValue($event.target.value, {
      onlySelf: true,
    });
  }
  onSubmit() {
    if (this.inviteForm.invalid) {
      this.alertService.error(`Please check your input`, this.options);
      return;
    }
    const inviteUser = this.inviteForm.value;
    this.userService.inviteUser(inviteUser).subscribe(
      () => {
        this.alertService.success(`${this.inviteForm.get("name").value.toString()} invite successfully!!!`, this.options);
        this.toggleModal();
      },
      error => {
        this.alertService.error(`Email: ${error?.email[0]}`, this.options);
        this.toggleModal();
      }
    )
  }
}
