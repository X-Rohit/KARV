function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else if (input == "what is ipo") {
        return "Initial Public Offering (IPO) refers to the process where private companies sell their shares to the public to raise equity capital from the public investors. The process of IPO transforms a privately-held company into a public company. This process also creates an opportunity for smart investors to earn a handsome return on their investments.";
    } else if (input == "what is FandO") {
        return "Futures and options are financial derivatives that allow traders to speculate on the price movements of an underlying asset without actually owning it. Futures contracts obligate the buyer to purchase an underlying asset, while the seller must deliver it at a predetermined price and date.";
    }
    else if (input == "what is intraday") {
        return "Purchasing and selling securities listed in a stock exchange on the same day is known as intraday trading. The primary purpose of transacting in this method is to realise capital gains on purchased securities as well as minimise risks by keeping money invested for an extended period.";
    }
    else if (input == "what is long term invesment") {
        return "A long-term investment is an account a company plans to keep for at least a year such as stocks, bonds, real estate, and cash. The account appears on the asset side of a company's balance sheet. Long-term investors are generally willing to take on more risk for higher rewards.";
    } 
    else if (input == "what is top gainers") {
        return "Gainers are the stocks that tend to close with a higher price than what they opened with/their previous close price in an intraday market. If they are a part of any indices, the market indices shoot up.";
    }
    else if (input == "what is top losers") {
        return "A loser is a secutiry with a high price at the open or at the start of a trading day versus its price at the end of the trading day. When the stock market indexes slump down across the board, it is likely that there will be more losers than gainers in the market.";
    }                
    else if (input == "what is mutual funds") {
        return "A mutual fund is a company that pools money from many investors and invests the money in securities such as stocks, bonds, and short-term debt. The combined holdings of the mutual fund are known as its portfolio. Investors buy shares in mutual funds. Each share represents an investors part ownership in the fund and the income it generates.";
    }
    else if (input == "difference between fundamental and technical analysis") {
        return "Technical analysis looks at the price movement of a security and uses this data to attempt to predict future price movements. Fundamental analysis instead looks at economic and financial factors that influence a business.";
    }
    else if (input == "what is tax saving") {
        return "A tax saving is a reduction in the amount of taxes paid by an individual, business, or other taxpayers. This can result in a reduction of income tax withholding or total tax liability after filing an income tax return. Tax savings often results from deductions, exemptions, and credits.";
    }
    else if (input == "what is meant by tiker") {
        return "";
    }
    else if (input == "which is the most useful indicator") {
        return "moving average,Exponential moving average,Stochastic oscillator,Moving average convergence divergence,Bollinger bands,Relative strength index";
    }
    else if (input == "how to purchase a stock") {
        return"1.Open a Demat account 2.Understand stock quotes 3.Bids and asks 4.Fundamental and technical knowledge of stock  5.Learn to stop the loss  6.Ask an expert  7.Start with safer stocks";
    }
    else if (input == "when to sell a stock") {
        return"The best time anyone can sell their stock in the Indian stock market is at the start of the day, which is between 9:30 Am to 10:00 Am. This is because, in the morning, people are more likely to buy stocks and invest in them.";
    }
    else if (input == "fundamentals of stock market") {
        return"";    
    }
    else if (input == "how to make profit in stock market") {
        return"Know the kind of a trader you are ,Try and avoid the herd mentality ,Never try to time the stock market , Have a disciplined approach for investment , Always have realistic goals";
    }         

    else {
        return "Try asking something else!";
    }
}