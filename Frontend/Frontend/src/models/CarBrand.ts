import { Car } from "./Car";


export interface CarBrand{

    id:number;
    CarBrand:string;
    Founded:string;
    CEO:string;
    NumberOFEmployees:number;
    NetIncome:string;
    cars:Car[];
}