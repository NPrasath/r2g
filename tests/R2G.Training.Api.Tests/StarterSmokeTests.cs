using System.Net;
using System.Text.Json;
using Microsoft.AspNetCore.Mvc.Testing;
using Xunit;

namespace R2G.Training.Api.Tests;

public sealed class StarterSmokeTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly WebApplicationFactory<Program> factory;

    public StarterSmokeTests(WebApplicationFactory<Program> factory)
    {
        this.factory = factory;
    }

    [Theory]
    [InlineData("/", "stage", "starter")]
    [InlineData("/health", "status", "ok")]
    public async Task Starter_boots_and_serves_expected_json(
        string path, string property, string expected)
    {
        using var client = factory.CreateClient();
        using var response = await client.GetAsync(path);

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        Assert.Equal("application/json", response.Content.Headers.ContentType?.MediaType);
        using var json = JsonDocument.Parse(await response.Content.ReadAsStringAsync());
        Assert.Equal(expected, json.RootElement.GetProperty(property).GetString());
    }
}
