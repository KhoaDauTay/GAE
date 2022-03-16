import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";

// layouts
import { AdminComponent } from "./layouts/admin/admin.component";

// admin views
import { DashboardComponent } from "./views/admin/dashboard/dashboard.component";
import { ProfileComponent } from "./views/admin/profile/profile.component";
import { UsersComponent } from "./views/admin/tables/tables.component";

// auth views

// no layouts views
import { IndexComponent } from "./views/index/index.component";

// components for views and layouts

import { AdminNavbarComponent } from "./components/navbars/admin-navbar/admin-navbar.component";
import { CardBarChartComponent } from "./components/cards/card-bar-chart/card-bar-chart.component";
import { CardLineChartComponent } from "./components/cards/card-line-chart/card-line-chart.component";
import { CardPageVisitsComponent } from "./components/cards/card-page-visits/card-page-visits.component";
import { CardProfileComponent } from "./components/cards/card-profile/card-profile.component";
import { CardSettingsComponent } from "./components/cards/card-settings/card-settings.component";
import { CardSocialTrafficComponent } from "./components/cards/card-social-traffic/card-social-traffic.component";
import { CardStatsComponent } from "./components/cards/card-stats/card-stats.component";
import { CardTableComponent } from "./components/cards/card-table/card-table.component";
import { FooterAdminComponent } from "./components/footers/footer-admin/footer-admin.component";
import { FooterComponent } from "./components/footers/footer/footer.component";
import { HeaderStatsComponent } from "./components/headers/header-stats/header-stats.component";
import { IndexNavbarComponent } from "./components/navbars/index-navbar/index-navbar.component";
import { TableDropdownComponent } from "./components/dropdowns/table-dropdown/table-dropdown.component";
import { NotificationDropdownComponent } from "./components/dropdowns/notification-dropdown/notification-dropdown.component";
import { SidebarComponent } from "./components/sidebar/sidebar.component";
import { UserDropdownComponent } from "./components/dropdowns/user-dropdown/user-dropdown.component";
import { NG_ENTITY_SERVICE_CONFIG } from "@datorama/akita-ng-entity-service";
import { AkitaNgDevtools } from "@datorama/akita-ngdevtools";
import { AkitaNgRouterStoreModule } from "@datorama/akita-ng-router-store";
import { environment } from "../environments/environment";
import {AuthenticationModule} from "./authentication/authentication.module";
import {HttpClientModule} from "@angular/common/http";
import {ApplicationModule} from "./applications/application.module";
import {AlertModule} from "./alert";

@NgModule({
    declarations: [
        AppComponent,
        DashboardComponent,
        CardBarChartComponent,
        CardLineChartComponent,
        TableDropdownComponent,
        NotificationDropdownComponent,
        UserDropdownComponent,
        SidebarComponent,
        FooterComponent,
        FooterAdminComponent,
        CardPageVisitsComponent,
        CardProfileComponent,
        CardSettingsComponent,
        CardSocialTrafficComponent,
        CardStatsComponent,
        CardTableComponent,
        HeaderStatsComponent,
        AdminNavbarComponent,
        IndexNavbarComponent,
        AdminComponent,
        ProfileComponent,
        UsersComponent,
        IndexComponent,
    ],
    imports: [
        BrowserModule,
        HttpClientModule,
        AuthenticationModule,
        ApplicationModule,
        AlertModule,
        AppRoutingModule,
        environment.production ? [] : AkitaNgDevtools.forRoot(),
        AkitaNgRouterStoreModule
    ],
    providers: [{provide: NG_ENTITY_SERVICE_CONFIG, useValue: {baseUrl: "https://gae-gw.systems/api"}}],
    bootstrap: [AppComponent],
})
export class AppModule {}
