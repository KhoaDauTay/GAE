import { Injectable } from "@angular/core";
import { NgEntityService } from "@datorama/akita-ng-entity-service";
import { ApplicationsStore, ApplicationsState } from "./applications.store";

@Injectable({ providedIn: "root" })
export class ApplicationsService extends NgEntityService<ApplicationsState> {

  constructor(protected store: ApplicationsStore) {
    super(store);
  }

}
