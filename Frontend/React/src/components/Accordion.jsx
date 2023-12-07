import React from "react";
import QuestionCard from "./QuestionCard";

export default function Accordion() {
  return (
    <div className="accordion">
      <QuestionCard
        question="Ordering for Delivery?"
        answer="We offer convenient delivery services for your purchases. Whether you're looking to have your items delivered to your doorstep or sent as a thoughtful gift, we've got you covered. Please contact us for more information on delivery options and associated fees."
      />
      <QuestionCard
        question="Potting Services"
        answer="We offer potting on in store purchases or you are welcome to bring in your own and we can pot them for you: There is a fee depending one what supplies are used. Visit us or call us for more details."
      />
      <QuestionCard
        question="Do we Ship Plants?"
        answer="Yes, we provide plant shipping services to ensure your green companions reach you safely. We take great care in packaging and handling your plants for a secure journey. Feel free to get in touch with us for details on plant shipping and associated costs."
      />
      <QuestionCard
        question="Ordering for Pick up?"
        answer="If you prefer to pick up your purchases in person, that's not a problem at all. We offer convenient in-store pick-up options. Simply place your order and select the pick-up option, and we'll have everything ready for you. For any specific requirements or details, please reach out to us."
      />
    </div>
  );
}
