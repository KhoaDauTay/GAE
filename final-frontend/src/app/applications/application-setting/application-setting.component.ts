import {Component, OnInit} from "@angular/core";
import {ActivatedRoute} from "@angular/router";
import {ApplicationsQuery} from "../state/applications.query";
import {ApplicationsService} from "../state/applications.service";
import {Application} from "../state/application.model";
import {FormBuilder, Validators} from "@angular/forms";
import {AlertService} from "../../alert";

@Component({
  selector: "app-application-setting",
  templateUrl: "./application-setting.component.html",
})
export class ApplicationSettingComponent implements OnInit {
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  constructor(
    private route: ActivatedRoute,
    private applicationQuery: ApplicationsQuery,
    private applicationService: ApplicationsService,
    private readonly formBuilder: FormBuilder,
    public alertService: AlertService
  ) {
  }
  applicationForm = this.formBuilder.group({
    name: ["", Validators.required],
    redirect_uris: ["", Validators.required],
    client_type: [""],
    authorization_grant_type: [""],
    scopes: [""]
  });
  application: Application
  applicationId: string;
  grantTypes: Array<string> = [ "authorization-code", "implicit", "password", "client-credentials", "openid-hybrid" ]
  clientTypes: Array<string> = [ "confidential", "public" ]
  defaultGrantType: string;
  defaultClientType: string;
  selectedScopes = [];
  scopes: any;
  ngOnInit(): void {
    this.applicationService.get(this.applicationId).subscribe(
      () => {
        this.applicationId = this.route.snapshot.paramMap.get("id");
        this.application = this.applicationQuery.getEntity(this.applicationId);
        this.defaultGrantType = this.application.authorization_grant_type;
        this.grantTypes.forEach((grantType,index)=>{
          if(grantType === this.defaultGrantType){
            this.grantTypes.splice(index,1);
          }
        });
        this.defaultClientType = this.application.client_type;
        this.clientTypes.forEach((clientType,index)=>{
          if(clientType === this.defaultClientType){
            this.clientTypes.splice(index,1);
          }
        });
        this.loadFormGroup();
        this.selectedScopes = this.application.scopes;
      });
    this.loadScopes();
  }
  get grantTypeValue() {
    return this.applicationForm.get("authorization_grant_type");
  }
  get clientTypeValue() {
    return this.applicationForm.get("client_type");
  }
  onSubmit() {
    if (this.applicationForm.invalid) {
      console.log(this.applicationForm.invalid)
      this.alertService.error(`Please check your input`, this.options);
      return;
    }
    this.applicationForm.patchValue(
      {
        scopes: this.convertScopes(),
      }
    );
    const applicationUpdate: Partial<Application> = this.applicationForm.value;
    this.applicationService.update(this.applicationId, applicationUpdate).subscribe(
      (() => {
        this.alertService.success(`${this.applicationForm.get("name").value.toString()} update successfully!!!`, this.options)})
    )
  }

  changeGrantType($event: any) {
    this.grantTypeValue?.setValue($event.target.value, {
      onlySelf: true,
    });
  }
  changeClientType($event: any) {
    this.clientTypeValue?.setValue($event.target.value, {
      onlySelf: true,
    });
  }
  loadScopes() {
    this.applicationService.getRoles().subscribe(
      (result) => this.scopes = result
    )
  }
  loadFormGroup(){
    this.applicationForm.setValue(
      {
        name: this.application.name,
        redirect_uris: this.application.redirect_uris,
        client_type: this.application.client_type,
        authorization_grant_type: this.application.authorization_grant_type,
        scopes: "",
      }
    );
  }
  convertScopes(){
    return this.selectedScopes.join(" ");
  }
}
