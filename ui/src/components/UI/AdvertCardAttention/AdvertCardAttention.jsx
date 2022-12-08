import React from "react";
import Img from "../../../assets/img/20c74a6fd59a8dd8bb8277f84f0aea2b.jpg";
import BookmarkIcon from "../../../assets/icons/bookmark-icon.svg";

export const AdvertCardAttention = () => {
    return (
        <div className="advert-attention group/advert-attention">
            <div className="attention-box ">
                <div className="attention-img ">
                    <img src={Img} alt="" />
                    <div className="advert-price ">
                        <p>
                            45555554 <span>$</span>
                        </p>
                    </div>
                    <button className="advert-bookmark  group-hover/advert-attention:opacity-100 opacity-30">
                        <img src={BookmarkIcon} alt="Добавить в избранное" />
                    </button>
                </div>
                <div className="advert-desc">
                    <h4>
                        Lorem ipsum dolor, sit amet consectetur adipisicing
                        elit. Aliquid amet saepe laborum vel modi eligendi
                        aliquam voluptas aut? Incidunt, laudantium officiis
                        consequuntur impedit aliquam quibusdam qui alias
                        repudiandae molestias dolorem!
                    </h4>
                    <p className="">
                        <span>Сгодня 14:00</span>
                        <span>Приднестровье, Тирасполь</span>
                    </p>
                </div>
            </div>
        </div>
    );
};
