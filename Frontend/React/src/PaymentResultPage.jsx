import { Outlet } from 'react-router-dom'

const PaymentResultPage = () => {
  const styles = {
    backgroundImage: `url('/collections-bg.jpg')`,
  };
  
  return (
    <section className="payment" style={styles}>
      <Outlet />
    </section>
  )
}

export default PaymentResultPage