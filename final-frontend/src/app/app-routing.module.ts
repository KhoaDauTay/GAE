import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

// layouts
import { AdminComponent } from "./layouts/admin/admin.component";

// admin views
import { DashboardComponent } from "./views/admin/dashboard/dashboard.component";
import { ProfileComponent } from "./views/admin/profile/profile.component";
import {UsersComponent} from "./views/admin/tables/tables.component";

// auth views
import { LoginComponent } from "./authentication/login/login.component";

// no layouts views
import { IndexComponent } from "./views/index/index.component";
import {AuthenticationGuard} from "./authentication/services";
import {ApplicationsComponent} from "./applications/applications.component";
import {ApplicationSettingComponent} from "./applications/application-setting/application-setting.component";
import {ApplicationCreateComponent} from "./applications/application-create/application-create.component";

const routes: Routes = [
  // admin views
  {
    path: "admin",
    component: AdminComponent,
    canActivate: [AuthenticationGuard],
    children: [
      { path: "dashboard", component: DashboardComponent },
      { path: "profile", component: ProfileComponent },
      { path: "users", component: UsersComponent },
      { path: "applications", component: ApplicationsComponent },
      { path: "applications/create", component: ApplicationCreateComponent },
      { path: "applications/:id", component: ApplicationSettingComponent },
      { path: "", redirectTo: "dashboard", pathMatch: "full" },
    ],
  },
  { path: "login", component: LoginComponent },
  // no layout views
  { path: "", component: IndexComponent },
  { path: "**", redirectTo: "", pathMatch: "full" },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
