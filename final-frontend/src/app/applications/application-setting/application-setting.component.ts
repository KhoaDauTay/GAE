import { Component, OnInit } from "@angular/core";
import {ActivatedRoute} from "@angular/router";
import {ApplicationsQuery} from "../state/applications.query";
import {ApplicationsService} from "../state/applications.service";
import {Application} from "../state/application.model";

@Component({
  selector: "app-application-setting",
  templateUrl: "./application-setting.component.html",
})
export class ApplicationSettingComponent implements OnInit {
  application: Application
  constructor(
    private route: ActivatedRoute,
    private applicationQuery: ApplicationsQuery,
    private applicationService: ApplicationsService
  ) {
  }
  applicationId: string;
  ngOnInit(): void {
    this.applicationService.get(this.applicationId).subscribe(
      () => {
        this.applicationId = this.route.snapshot.paramMap.get("id");
        this.application = this.applicationQuery.getEntity(this.applicationId);
      });

  }

}
