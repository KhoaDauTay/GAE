import { Injectable } from "@angular/core";
import { EntityState, EntityStore, StoreConfig } from "@datorama/akita";
import { Application } from "./application.model";

export interface ApplicationsState extends EntityState<Application> {}

@Injectable({ providedIn: "root" })
@StoreConfig({ name: "applications" })
export class ApplicationsStore extends EntityStore<ApplicationsState> {

  constructor() {
    super();
  }

}
