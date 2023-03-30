import { Car } from "./Car";

export interface Owner{

    id:number;
    LastName:string;
    FirstName:string;
    CNP:string;
    Email:string;
    Address:string;
    cars:Car[];
}