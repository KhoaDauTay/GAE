import {Component, OnInit} from "@angular/core";
import {FormBuilder, Validators} from "@angular/forms";
import {ApplicationsService} from "../state/applications.service";
import {AlertService} from "../../alert";
import {Application} from "../state/application.model";

@Component({
  selector: "app-application-create",
  templateUrl: "./application-create.component.html",
})
export class ApplicationCreateComponent implements OnInit {
  showModal = false;
  options = {
    autoClose: true,
    keepAfterRouteChange: false
  };
  applicationForm = this.formBuilder.group({
    name: ["", Validators.required],
    redirect_uris: ["", Validators.required],
    client_type: [""],
    authorization_grant_type: [""],
    scopes: [""]
  });
  grantTypes: Array<string> = ["authorization-code", "implicit", "password", "client-credentials", "openid-hybrid" ]
  clientTypes: Array<string> = ["confidential", "public"]
  defaultGrantType: string;
  defaultClientType: string;
  constructor(
    private formBuilder: FormBuilder,
    private applicationService: ApplicationsService,
    public alertService: AlertService) {
  }
  ngOnInit(): void {
    this.defaultGrantType = "authorization-code";
    this.grantTypes.forEach((grantType,index)=>{
      if(grantType === this.defaultGrantType){
        this.grantTypes.splice(index,1);
      }
    });
    this.defaultClientType = "confidential";
    this.clientTypes.forEach((clientType,index)=>{
      if(clientType === this.defaultClientType){
        this.clientTypes.splice(index,1);
      }
    });
    this.loadFormGroup();
  }
  toggleModal(){
    this.showModal = !this.showModal;
  }
  get grantTypeValue() {
    return this.applicationForm.get("authorization_grant_type");
  }
  get clientTypeValue() {
    return this.applicationForm.get("client_type");
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
  loadFormGroup(){
    this.applicationForm.setValue(
      {
        name: "Example name",
        redirect_uris: "https://example.com/callback",
        client_type: this.defaultClientType,
        authorization_grant_type: this.defaultGrantType,
        scopes: "users:me"
      }
    );
  }

  onSubmit() {
    if (this.applicationForm.invalid) {
      this.alertService.error(`Please check your input`, this.options);
      return;
    }
    const newApplication: Application = this.applicationForm.value;
    this.applicationService.add(newApplication).subscribe(
      (() => {
        this.alertService.success(`${this.applicationForm.get("name").value.toString()} create successfully!!!`, this.options);
        this.toggleModal();
      })
    )
  }
}
