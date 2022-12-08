import React from "react";
import { Routers } from "../../routes/Routers";
import { Header } from "../Header/Header";

export const Layout = () => {
    return (
        <div>
            <Header />

            <Routers />
        </div>
    );
};
