import { Component, OnInit } from "@angular/core";
import {FormBuilder, Validators} from "@angular/forms";
import {AlertService} from "../../alert";
import {ActivatedRoute} from "@angular/router";
import {RolesService} from "../state/roles.service";
import {RolesQuery} from "../state/roles.query";
import {Role} from "../state/role.model";
import {ApplicationsService} from "../../applications/state/applications.service";

@Component({
  selector: "app-role-setting",
  templateUrl: "./role-setting.component.html",
})
export class RoleSettingComponent implements OnInit {
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  constructor(
    private route: ActivatedRoute,
    private readonly formBuilder: FormBuilder,
    public alertService: AlertService,
    private roleService: RolesService,
    private applicationService: ApplicationsService,
    private roleQuery: RolesQuery
  ) { }
  roleForm = this.formBuilder.group({
    name: ["", [Validators.required, Validators.pattern("[A-Z]+$")]],
    description: ["", Validators.required],
    scopes: [""]
  });
  role: Role;
  roleId: string | number;
  selectedScopes = [];
  scopes: any;
  ngOnInit(): void {
    this.roleId = this.route.snapshot.paramMap.get("id")
    this.roleService.get(this.roleId).subscribe(
      () => {
        this.role = this.roleQuery.getEntity(this.roleId)
        this.loadFormGroup();
        this.selectedScopes = this.role.scopes;
      }
    )
    this.loadScopes();
  }

  private loadFormGroup() {
    this.roleForm.setValue(
      {
        name: this.role.name,
        description: this.role.description,
        scopes: "",
      }
    );
  }
  loadScopes() {
    this.applicationService.getRoles().subscribe(
      (result) => this.scopes = result
    )
  }

  onSubmit() {
    if (this.roleForm.invalid) {
      this.alertService.error(`Please check your input`, this.options);
      return;
    }
    this.roleForm.patchValue(
      {
        scopes: this.selectedScopes,
      }
    );
    const roleUpdate: Role = this.roleForm.value;
    this.roleService.update(this.roleId, roleUpdate).subscribe(
      () => {
        this.alertService.success(`${this.roleForm.get("name").value.toString()} update successfully!!!`, this.options);
      },
      error => {
        this.alertService.error(`Name: ${error?.name[0]}`, this.options);
      }
    )
  }
}
