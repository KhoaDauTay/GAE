import {NgModule} from "@angular/core";
import {CommonModule} from "@angular/common";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {RouterModule} from "@angular/router";
import {ApplicationsComponent} from "./applications.component";
import {CardApplicationComponent} from "./card-application/card-application.component";
import {ApplicationDropdownComponent} from "./application-dropdown/application-dropdown.component";
import {ApplicationSettingComponent} from "./application-setting/application-setting.component";
import {NgSelectModule} from "@ng-select/ng-select";
import { ApplicationCreateComponent } from "./application-create/application-create.component";
import { ApplicationDeleteComponent } from "./application-delete/application-delete.component";

@NgModule({
  declarations: [
    ApplicationsComponent,
    CardApplicationComponent,
    ApplicationDropdownComponent,
    ApplicationSettingComponent,
    ApplicationCreateComponent,
    ApplicationDeleteComponent,
  ],
  exports: [
    ApplicationsComponent
  ],
  imports: [
    FormsModule,
    CommonModule,
    ReactiveFormsModule,
    RouterModule,
    NgSelectModule,
  ]
})
export class ApplicationModule { }
