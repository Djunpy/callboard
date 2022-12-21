import React from "react";
import Logo from "../../assets/img/logo.png";

const Footer = () => {
    return (
        <footer className="footer ">
            <div className="footer-box ">
                <div className="footer-logo">
                    <img className="w-28" src={Logo} alt="" />
                </div>
                <div className="footer-info ">
                    <ul className="footer-list ">
                        <h4>Помощь</h4>
                        <li>Центр поддержки Djunpy</li>
                        <li>Советы по безопасности</li>
                        <li>FAQ</li>
                    </ul>
                    <ul className="footer-list">
                        <h4>Помощь</h4>
                        <li>Центр поддержки Djunpy</li>
                        <li>Советы по безопасности</li>
                        <li>FAQ</li>
                    </ul>
                    <ul className="footer-list">
                        <h4>Помощь</h4>
                        <li>Центр поддержки Djunpy</li>
                        <li>Советы по безопасности</li>
                        <li>FAQ</li>
                    </ul>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
