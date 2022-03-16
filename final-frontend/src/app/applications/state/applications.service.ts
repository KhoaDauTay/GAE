import { Injectable } from "@angular/core";
import { NgEntityService } from "@datorama/akita-ng-entity-service";
import { ApplicationsStore, ApplicationsState } from "./applications.store";
import {HttpClient} from "@angular/common/http";
import {tap} from "rxjs/operators";

@Injectable({ providedIn: "root" })
export class ApplicationsService extends NgEntityService<ApplicationsState> {

  constructor(protected store: ApplicationsStore) {
    super(store);
  }
  getRoles(){
    const http: HttpClient = this.getHttp();
    return http.get(`${this.baseUrl}/applications/get-roles`).pipe(
      tap(
        (data) => console.log(data),
      (error) => console.log(error),
      ),)
  }
}
