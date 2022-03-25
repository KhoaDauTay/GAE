import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { RolesComponent } from "./roles.component";
import { CardRoleComponent } from "./card-role/card-role.component";
import { RoleDropdownComponent } from "./role-dropdown/role-dropdown.component";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {RouterModule} from "@angular/router";
import {NgSelectModule} from "@ng-select/ng-select";
import { RoleSettingComponent } from "./role-setting/role-setting.component";
import { RoleCreateComponent } from "./role-create/role-create.component";



@NgModule({
  declarations: [
    RolesComponent,
    CardRoleComponent,
    RoleDropdownComponent,
    RoleSettingComponent,
    RoleCreateComponent
  ],
  imports: [
    FormsModule,
    CommonModule,
    ReactiveFormsModule,
    RouterModule,
    NgSelectModule,
  ]
})
export class RolesModule { }
