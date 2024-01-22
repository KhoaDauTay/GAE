import { Injectable } from "@angular/core";
import { QueryEntity } from "@datorama/akita";
import { ApplicationsStore, ApplicationsState } from "./applications.store";

@Injectable({ providedIn: "root" })
export class ApplicationsQuery extends QueryEntity<ApplicationsState> {

  constructor(protected store: ApplicationsStore) {
    super(store);
  }

}
