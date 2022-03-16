import {NgModule} from "@angular/core";
import {CommonModule} from "@angular/common";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {RouterModule} from "@angular/router";
import {ApplicationsComponent} from "./applications.component";
import {CardApplicationComponent} from "./card-application/card-application.component";
import {ApplicationDropdownComponent} from "./application-dropdown/application-dropdown.component";
import {ApplicationSettingComponent} from "./application-setting/application-setting.component";
import {NgSelectModule} from "@ng-select/ng-select";

@NgModule({
  declarations: [
    ApplicationsComponent,
    CardApplicationComponent,
    ApplicationDropdownComponent,
    ApplicationSettingComponent,
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
