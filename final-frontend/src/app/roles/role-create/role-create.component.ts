import { Component, OnInit } from "@angular/core";
import {FormBuilder, Validators} from "@angular/forms";
import {AlertService} from "../../alert";
import {RolesService} from "../state/roles.service";
import {Role} from "../state/role.model";

@Component({
  selector: "app-role-create",
  templateUrl: "./role-create.component.html",
})
export class RoleCreateComponent implements OnInit {
  showModal = false;
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  roleForm = this.formBuilder.group({
    name: ["", [Validators.required, Validators.pattern("[A-Z]+$")]],
    description: ["", Validators.required],
    scopes: [""]
  });
  constructor(
    private formBuilder: FormBuilder,
    public alertService: AlertService,
    private roleService: RolesService
  ) { }

  ngOnInit(): void {
    this.loadFormGroup();
  }
  toggleModal(){
    this.showModal = !this.showModal;
  }
  private loadFormGroup() {
    this.roleForm.setValue(
      {
        name: "NAME",
        description: "Write something",
        scopes: ["users:me"],
      }
    );
  }

  onSubmit() {
    if (this.roleForm.invalid) {
      this.alertService.error(`Please check your input`, this.options);
      return;
    }
    const roleCreate: Role = this.roleForm.value;
    this.roleService.add(roleCreate).subscribe(
      () => {
        this.toggleModal()
        this.alertService.success(`${this.roleForm.get("name").value.toString()} update successfully!!!`, this.options);
      },
      error => {
        this.toggleModal()
        this.alertService.error(`Name: ${error?.error?.name[0]}`, this.options);
      }
    )
  }
}
